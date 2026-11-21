# Инструкция. Задание 7 — Secret в поде

**Цель:** подключить Secret к приложению через отдельные ключи.

---

## Ход работы

### Шаг 1. Заполните шаблон

`templates/deployment-secret.yaml`: имя Secret и ключи
(`username` → `DB_USER`, `password` → `DB_PASSWORD`).

```bash
kubectl apply -f templates/deployment-secret.yaml
kubectl rollout status deployment/calc-app -n demo
```

### Шаг 2. Проверьте через приложение

```bash
kubectl port-forward deployment/calc-app 5000:5000 -n demo &
curl http://localhost:5000/config
```

Ожидается: db_user и db_password подставились.

### Шаг 3. Проверьте изнутри

```bash
kubectl exec deployment/calc-app -n demo -- env | grep DB_
```

Secret внутри пода читается открытым текстом.

### Шаг 4. Подумайте

`APP_NAME` снова стал `calc-app` — почему? Посмотрите на шаблон
deployment-secret.yaml: чего в нём нет по сравнению с заданием 3?
Как вернуть обе конфигурации сразу (envFrom + env)?

## Что сдать в отчёте

Вывод /config, ответ из шага 4 (и, если сделали, рабочий манифест
с обеими конфигурациями).
