# Инструкция. Задание 10 — Selector и endpoints: ломаем и чиним

**Цель:** понять связку Service ↔ Pod через labels — на поломке.

---

## Ход работы

### Шаг 1. Посмотрите endpoints

```bash
kubectl describe svc calc-service -n demo | grep -A3 Endpoints
```

Там IP работающих подов.

### Шаг 2. Сломайте

Измените selector сервиса на несуществующий label:

```bash
kubectl patch svc calc-service -n demo \
  -p '{"spec":{"selector":{"app":"net-takogo"}}}'
kubectl describe svc calc-service -n demo | grep -A3 Endpoints
```

### Шаг 3. Проверьте доступность

```bash
kubectl run curl-test --rm -i --image=curlimages/curl -n demo \
  --restart=Never --quiet -- curl -s --max-time 5 "http://calc-service/health"
```

Пусто/таймаут. Почему сервис «пустой», хотя поды живы?

### Шаг 4. Почините

Верните правильный selector той же командой patch (label `calc-app`).

## Что сдать в отчёте

Скриншот/вывод endpoints до и после поломки и ответ: что связывает
Service с подами?

## Частые проблемы

| Симптом | Решение |
|---|---|
| endpoints `<none>` | selector не совпадает с labels подов |
