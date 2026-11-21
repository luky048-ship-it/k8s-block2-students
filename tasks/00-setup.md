# Инструкция. Задание 0 — проверка окружения

**Цель:** убедиться, что всё из блока 1 осталось рабочим, и подготовить
образ v2 и ingress-контроллер.

---

## Шаги

```bash
kubectl get nodes                          # minikube Ready
kubectl get pods -A | head                 # системные поды живы
```

Сборка и загрузка образа v2 (из папки блока 2):

```bash
docker build -t calc-app:v2 app/
minikube image load calc-app:v2
minikube addons enable ingress             # понадобится в задании 5
kubectl create namespace demo              # если не существует
```

✔ **Контрольная точка:** `minikube image ls | grep calc-app` показывает
и `v1`, и `v2`; `minikube addons list | grep ingress` → enabled.

## Частые проблемы

| Симптом | Решение |
|---|---|
| `minikube: command not found` | повторите установку из блока 1, task 00 |
| кластер остановлен | `minikube start --driver=docker` |
| ingress addon долго включается | норма до 1–2 минут: качается контроллер |
