Версия в index.html (span.form-version в h1 и в легенде)

1) Локально (перед каждым коммитом)
   Выполните один раз в корне клона:

     Windows (PowerShell):  .\scripts\install-git-hooks.ps1
     Linux/macOS:           sh scripts/install-git-hooks.sh

   либо вручную:

     git config core.hooksPath .githooks

   Хук pre-commit снова делает git add index.html.
   На Windows (Git Bash) сначала вызывается bump-form-version.ps1 или py -3, затем python3/python —
   чтобы не попасть на заглушку Microsoft Store (WindowsApps\python.exe).
   На Linux/macOS — python3/python, затем PowerShell при необходимости.

2) На GitHub (если хук не настроен)
   Создайте в репозитории файл .github/workflows/bump-page-version.yml (содержимое скопируйте из
   contrib/bump-page-version.github-action.yml в корне проекта). После push в master workflow
   сравнивает vN с HEAD~1; если версия не выросла — делает +1 и пушит коммит с пометкой [page-version]
   в сообщении (такой коммит не обрабатывается повторно).
