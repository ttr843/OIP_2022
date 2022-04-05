<!doctype html>
<html lang="en">
<head>
    <title>Поиск</title>
</head>
<body>
<div>
    <a href="/main">
        <button type="submit" name="main">
            Перейти на страницу поиска
        </button>
    </a>
</div>
<div>
    <h3>Поиск</h3>
    <div>
        <#list resultMap?keys as key>
            <h5>Название файла: ${key}, значение: ${resultMap[key]}</h5>
            <p></p>
        </#list>
    </div>
</div>
</form>
</div>
</body>
</html>