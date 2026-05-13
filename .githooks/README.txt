Чтобы версия в легенде формы сама увеличивалась при коммите с index.html, один раз в клоне репозитория выполните:

  git config core.hooksPath .githooks

После этого при каждом коммите, куда входит изменённый index.html, хук pre-commit увеличит число в <span class="form-version">vN</span> и снова проиндексирует файл.
