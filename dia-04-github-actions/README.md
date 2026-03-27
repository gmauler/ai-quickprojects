# Dia 4 — GitHub Actions: lint automático

Workflow que corre automaticamente a cada push e verifica 
a qualidade do código Python com o ruff.

## Como funciona
1. Fazes `git push`
2. O GitHub deteta o ficheiro `.github/workflows/lint.yml`
3. Cria uma máquina virtual Ubuntu
4. Instala o ruff e verifica todos os ficheiros `.py`
5. Se houver erros, o workflow falha e és notificado