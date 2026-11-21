# Инструкция. Задание 6 — Secret: создаём и вскрываем

**Цель:** создать Secret и собственными руками доказать, что base64 —
не защита.

---

## Ход работы

### Шаг 1. Создайте Secret

```bash
kubectl create secret generic db-credentials \
  --from-literal=username=calc_user \
  --from-literal=password=s3cret-pass \
  -n demo
```

### Шаг 2. «Взломайте» сами себя

```bash
kubectl get secret db-credentials -n demo -o yaml
```

Найдите password в base64. Декодируйте:

```bash
kubectl get secret db-credentials -n demo -o jsonpath='{.data.password}' | base64 -d
```

### Шаг 3. Подумайте

Письменно: если base64 не защищает, зачем вообще Secret? Что реально
ограничивает доступ к нему? (Подсказка: подумайте про права доступа
к API кластера — кто может выполнить команду из шага 2.)

✔ **Контрольная точка:** можете объяснить, чем Secret лучше ConfigMap
и чем он НЕ лучше.

## Что сдать в отчёте

Декодированный пароль и ответ из шага 3.
