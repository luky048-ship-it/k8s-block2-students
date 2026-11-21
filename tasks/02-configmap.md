# Инструкция. Задание 2 — Создаём ConfigMap

**Цель:** вынести настройки в объект кластера.

---

## Ход работы

### Шаг 1. Заполните шаблон

`templates/configmap.yaml`: имя `calc-config`, namespace `demo`,
значения `APP_NAME: "calc-prod"`, `CALC_PRECISION: "4"`.

### Шаг 2. Подумайте перед применением

Почему `"4"` в кавычках? Попробуйте написать без кавычек
(`CALC_PRECISION: 4`) и выполнить:

```bash
kubectl apply -f templates/configmap.yaml --dry-run=client -o yaml
```

Прочитайте текст ошибки. Верните кавычки.

### Шаг 3. Примените и исследуйте

```bash
kubectl apply -f templates/configmap.yaml
kubectl get configmap calc-config -n demo -o yaml
```

Найдите в выводе свои ключи. Где физически хранится ConfigMap
(вспомните архитектуру из блока 1 — компонент control plane)?

✔ **Контрольная точка:** ConfigMap создан, знаете, где он хранится.

## Что сдать в отчёте

Ответ: почему значения только строки, и где хранится ConfigMap.
