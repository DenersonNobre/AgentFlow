# Quality Auditor Prompt
Analise a qualidade do código em lib/ de forma **rigorosa**:
1. Execute `flutter analyze lib/` — **0 erros, 0 warnings, 0 infos** são exigidos. Qualquer alerta (info, warning, error) em QUALQUER arquivo (lib/, test/, integration_test/) REPROVA a qualidade.
2. Execute `flutter test` — **100% dos testes devem passar**. Testes pulados ou falhos REPROVAM.
3. Verifique padrões arquiteturais (Clean Architecture, BLoC, Repository, injeção de dependência)
4. Gere `pipeline/quality-report.json` com a análise completa, listando cada alerta individualmente.
5. **Regra de ouro**: se houver QUALQUER alerta (error, warning, info) em qualquer arquivo, o status deve ser "reprovado".
