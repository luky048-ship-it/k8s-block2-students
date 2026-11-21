# Инструкция. Задание 3 — Подключаем ConfigMap через env

**Цель:** приложение меняет поведение без пересборки образа.

---

## Ход работы

### Шаг 1. Раскомментируйте envFrom

В `templates/deployment-v2.yaml` раскомментируйте блок `envFrom`
(с пояснением в файле), впишите имя ConfigMap из задания 2.

```bash
kubectl apply -f templates/deployment-v2.yaml
kubectl rollout status deployment/calc-app -n demo
```

### Шаг 2. Проверка

```bash
kubectl port-forward deployment/calc-app 5000:5000 -n demo &
curl http://localhost:5000/config
curl "http://localhost:5000/calc?op=div&a=10&b=3"
```

Ожидается: `calc-prod`, precision 4, деление с 4 знаками.

### Шаг 3. Докажите себе, что образ тот же

```bash
kubectl get pods -n demo -o jsonpath='{.items[*].spec.containers[*].image}'
```

Образ не менялся — только окружение.

✔ **Контрольная точка:** /config показывает значения из ConfigMap.

## Что сдать в отчёте

Вывод /config и вывод про образ.
