# Инструкция. Задание 4 — Живая смена конфигурации (ловушка)

**Цель:** натолкнуться на ограничение env-способа и понять его.

---

## Ход работы

### Шаг 1. Измените ConfigMap

В `templates/configmap.yaml` поставьте `CALC_PRECISION: "1"`,
примените: `kubectl apply -f templates/configmap.yaml`.

### Шаг 2. Проверьте /config

```bash
kubectl port-forward deployment/calc-app 5000:5000 -n demo &
curl http://localhost:5000/config
```

Изменилось? **Нет.** Не спешите чинить — сначала ответьте письменно:
почему? (Подсказки: когда процесс читает переменные окружения?
Пересоздавался ли под? `kubectl get pods -n demo` — возраст подов.)

### Шаг 3. Почините правильно

```bash
kubectl rollout restart deployment/calc-app -n demo
kubectl rollout status deployment/calc-app -n demo
curl http://localhost:5000/config
```

Теперь precision = 1.

### Шаг 4. Подумайте

Перезапуск подов в бою — это простой. Как бы вы меняли конфигурацию
без простоя, если приложение критичное? (Вспомните rolling update
из блока 1 — что делает `rollout restart` на самом деле?)

## Что сдать в отчёте

Ответы из шагов 2 и 4.
