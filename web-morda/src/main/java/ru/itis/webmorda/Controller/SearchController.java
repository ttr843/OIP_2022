package ru.itis.webmorda.Controller;

import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

/**
 * @author <a href="mailto:ruslan.pashin@waveaccess.ru">Ruslan Pashin</a>
 */
@Controller
@RequiredArgsConstructor
public class SearchController {


    private static final String URL = "http://localhost:8080";
    private final RestTemplate restTemplate = new RestTemplate();

    @GetMapping("/main")
    public String mainPage() {
        return "main";
    }

    @PostMapping("/search-request")
    public String createSearchRequest(String searchWords, Model model) {
        HttpEntity<String> result = restTemplate.getForEntity(
                String.format("%s/search?query=%s", URL, searchWords),
                String.class
        );
        Map<String, String> resultMap = new HashMap<>();
        for (String str: result.getBody().substring(1,result.getBody().length()-1).split(",")) {
            String[] keyValue = str.split(":");
            resultMap.put(keyValue[0], keyValue[1]);
        }
        model.addAttribute("resultMap", resultMap);
        return "result";
    }


}
