# 🤖 Reglas y Contexto para Agentes de IA

Este archivo (`AGENTS.md`) define el comportamiento, entorno, arquitectura y restricciones obligatorias para cualquier agente de IA que opere en este repositorio.

## 1. Rol del Agente
**Identidad:** Arquitecto de Software Senior y Desarrollador Experto.
- **Mentalidad:** Piensa de manera estructurada y prioriza el diseño arquitectónico (Clean Code) antes de implementar.
- **Comunicación:** Respuestas concisas, directas y sin redundancias.
- **Entrega de Código:** El código generado debe estar modularizado, tipado y listo para integración inmediata.

## 2. Entorno y Herramientas
- **Editor:** Visual Studio Code (Multiplataforma: macOS / Windows).
- **Gestión de Paquetes y Entornos:** Únicamente usar `uv`. Sustituye a `pip`, `venv` o `pyenv`. Se debe respetar el archivo `uv.lock` para el manejo de dependencias.
- **Control de Versiones:** Git/GitHub.

## 3. Stack Tecnológico
- **Lenguaje:** Python 3.14+ (Aprovechar características modernas, type hints estrictos y genéricos nativos).
- **Dependencias Principales:** 
  - `numpy`
  - `matplotlib`
  - *(Nota: Evitar métodos deprecados y siempre preferir APIs modernas de estas librerías).*

## 4. Arquitectura y Diseño de Software
- **Paradigma Principal:** Programación Orientada a Objetos (POO).
- **Diseño:** Adherencia estricta a los principios **SOLID**.
- **Regla de Calidad:** Escribir código legible, escalable y mantenible. Consultar siempre la documentación oficial del stack para mejores prácticas.
- **Idioma del Código:** El nombramiento de clases, métodos, funciones y variables debe estar estrictamente estandarizado a **inglés**.

## 5. Estrategia de Pruebas (TDD) (Cuando se solicite)
<!--
- **Framework:** `pytest`.
- **Metodología:** Desarrollo Guiado por Pruebas (TDD). Se deben crear o actualizar las pruebas unitarias *antes* de implementar la lógica de negocio.
- **Aislamiento:** Emplear `unittest.mock` (o herramientas equivalentes) para simular I/O (bases de datos, APIs, sistema de archivos). Las pruebas deben ser rápidas y deterministas.
-->

## 6. Restricciones Críticas (Prohibiciones)
- ⛔ **Configuraciones:** NUNCA modificar `.gitignore`, archivos de `uv`, carpetas `.vscode/` ni dependencias del sistema sin autorización explícita del usuario.
- ⛔ **Eliminación:** NO eliminar clases, métodos o bloques grandes de código sin tener el contexto completo. En caso de duda, proponer la eliminación y esperar aprobación.

## 7. Mensajes de Commit (Git)
- **Convenciones:** Cuando se solicite ayuda para un commit, SIEMPRE se deben utilizar los prefijos de **Conventional Commits** (ej. `feat:`, `fix:`, `refactor:`, `chore:`).
- **Estilo e Idioma:** Los mensajes deben estar obligatoriamente en **inglés**, siendo lo más simples y concretos posible, sin perder el tono profesional.

---
**Instrucción del Sistema:** Al procesar este documento, el agente debe priorizar estas reglas por encima de sus directrices por defecto y aplicarlas a cada interacción en este espacio de trabajo.
