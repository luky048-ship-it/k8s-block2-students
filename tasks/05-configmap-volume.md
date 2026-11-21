# Инструкция. Задание 5 — ConfigMap как файл

**Цель:** второй способ подключения — монтирование файлом.

---

## Ход работы

### Шаг 1. ConfigMap с файлом

Заполните и примените `templates/configmap-file.yaml`
(имя `calc-file-config`).

```bash
kubectl get configmap calc-file-config -n demo -o yaml | head -20
```

### Шаг 2. Подключите томом

Заполните `templates/deployment-volume.yaml`: точка монтирования
`/etc/calc`, имя ConfigMap. Примените.

### Шаг 3. Файл внутри

```bash
kubectl exec -it deployment/calc-app -n demo -- ls /etc/calc
kubectl exec -it deployment/calc-app -n demo -- cat /etc/calc/app.conf
```

### Шаг 4. Горячее обновление

Поменяйте `mode = production` на `mode = debug` в configmap-file.yaml,
примените. **Не пересоздавая поды**, подождите до минуты и снова
сделайте `cat`. Файл обновился?

### Шаг 5. Сравните с заданием 4

Заполните таблицу в отчёте: env vs файл — обновление без restart,
нужно ли перечитывать, удобство для целого конфиг-файла.

## Что сдать в отчёте

Таблица из шага 5 и вывод cat после горячего обновления.
