# Инструкция. Задание 14 — Ingress: правило для calc.local

**Цель:** опубликовать приложение по человеческому адресу.

---

## Ход работы

### Шаг 1. Заполните и примените

`templates/ingress.yaml`: хост `calc.local`, сервис `calc-service`,
порт 80.

```bash
kubectl apply -f templates/ingress.yaml
kubectl get ingress -n demo
```

### Шаг 2. Имя → адрес

```bash
echo "$(minikube ip) calc.local" | sudo tee -a /etc/hosts
```

### Шаг 3. Проверка

```bash
curl http://calc.local/health
curl "http://calc.local/calc?op=mul&a=6&b=7"
```

> **macOS + docker-драйвер:** IP minikube с хоста недоступен напрямую.
> Вариант А (как в жизни): `minikube tunnel` в отдельном терминале
> (спросит sudo) — тогда calc.local отвечает напрямую.
> Вариант Б (без sudo): проброс через контроллер —
> ```bash
> kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 18080:80 &
> curl -H "Host: calc.local" http://localhost:18080/health
> ```

✔ **Контрольная точка:** calc отвечает 42 по http://calc.local.

### Шаг 4. Нарисуйте путь запроса

В отчёт — цепочка: браузер → … → Pod (5 элементов).

## Что сдать в отчёте

Вывод curl и цепочка из шага 4.

## Частые проблемы

| Симптом | Решение |
|---|---|
| Could not resolve host | нет строки в /etc/hosts |
| 404 от nginx | service/port в правиле не совпали |
| нет ADDRESS у ingress | контроллер не поднялся (задание 13) |
