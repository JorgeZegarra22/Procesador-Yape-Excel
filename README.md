# ⚡ Procesador Yape Excel — Generador de Oportunidades para Sorteos

[![Astro][astro-badge]][astro-url]
[![TypeScript][typescript-badge]][typescript-url]
[![Tailwind CSS][tailwind-badge]][tailwind-url]
[![License: MIT][license-badge]][license-url]

🚀 **[¡PROBAR EN VIVO! — Demo en Netlify](https://yapeexcel.netlify.app/procesador-yape/)**

---

> **Procesador Yape Excel** es una herramienta administrativa y de análisis de datos de alto rendimiento desarrollada en **Astro**. Su objetivo principal es recibir reportes de movimientos oficiales de **Yape** en formato `.xlsx` o `.xls`, normalizar sus datos financieros en tiempo real, filtrar por criterios cronológicos específicos, calcular oportunidades/tickets de sorteos según montos consolidados, y generar bases planas optimizadas para plataformas de sorteos en vivo.


> [!IMPORTANT]
> **RECUERDA:** El sistema procesa y muestra **únicamente** las transacciones de tipo **TE PAGÓ** (dinero recibido). Las transacciones de tipo **PAGASTE** (dinero enviado) u otros egresos son descartados de forma automática para calcular oportunidades válidas.

---

## 📸 Guía Visual del Sistema

El procesador está diseñado como un asistente de 4 pasos interactivos que guían al administrador en la preparación de su sorteo:

### Paso 1: Carga y Lectura del Reporte de Yape
Sube tu reporte oficial descargado de Yape. El sistema utiliza **SheetJS** para realizar un parseo binario ultraveloz directamente en el navegador, omitiendo metadatos innecesarios del reporte y detectando de forma robusta la fila de encabezados y columnas de transacciones.
![Paso 1 - Carga de Reporte Excel](/public/GITHUB/1.png)

### Paso 2: Filtrado Cronológico y Definición del Ticket
Permite seleccionar una fecha específica del reporte (o procesarlas todas) y definir un filtro de hora de inicio (por ejemplo, considerar solo pagos recibidos de las `18:00` en adelante). También se define el valor en Soles (S/) de cada ticket u oportunidad para el cálculo matemático.
![Paso 2 - Filtro por Fecha, Hora y Valor de Ticket](/public/GITHUB/2.png)

### Paso 3: Consolidación y Gestión de Participantes
Consolida múltiples pagos realizados por un mismo usuario (identificado por su número u origen), calculando sus oportunidades de sorteo (`Monto Total / Valor del Ticket`) y detectando "Sobrantes" (dinero restante que no llega a completar otro ticket). En esta tabla puedes buscar participantes en tiempo real y **eliminar** usuarios observados, lo que recalcula instantáneamente los montos y pozos en vivo.
![Paso 3 - Resumen y Tabla de Participantes Consolidados](/public/GITHUB/3.png)

### Paso 4: Generación de Lista Plana y Exportación
Genera una lista plana de nombres repetidos según el número de oportunidades de cada uno. Ofrece un botón de un solo clic para **Copiar la Lista Completa** al portapapeles y proporciona accesos directos integrados con las plataformas de sorteo más populares y confiables del sector.
![Paso 4 - Generación de Lista Plana para Sorteos](/public/GITHUB/4.png)

---

## 🚀 Características Clave e Innovaciones

### 📊 1. Algoritmo Asíncrono por Chunks
Procesar reportes con miles de transacciones puede congelar la interfaz del navegador. Para solucionar esto, el sistema implementa un procesador por bloques o **chunks asíncronos**:
* Segmenta el array de datos en lotes pequeños (500 filas).
* Procesa cada lote de forma no bloqueante utilizando ciclos diferidos (`setTimeout`), liberando el hilo principal para que el navegador pueda repintar la UI.
* Muestra una barra de carga precisa que avanza en tiempo real mientras el sistema se mantiene interactivo y responsivo.

### 📅 2. Normalización Inteligente de Fechas
Los formatos de fecha varían en los reportes (objetos de fecha nativos de Excel, cadenas tipo `DD/MM/YYYY` o `DD-MM-YYYY`). El procesador normaliza estas variaciones de forma automática para permitir un filtrado dinámico por fecha y hora de operación sin fallos de parseo.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Propósito |
| :--- | :--- | :--- |
| **Framework** | [![Astro][astro-badge]][astro-url] | Arquitectura híbrida (SSR + SSG) e islas interactivas veloces. |
| **Lenguaje** | [![TypeScript][typescript-badge]][typescript-url] | Tipado estricto y solidez en el flujo de datos. |
| **Diseño** | [![Tailwind CSS][tailwind-badge]][tailwind-url] | Estética premium *dark-mode*, gradientes y micro-animaciones fluidas. |
| **Parseo XLS** | `SheetJS (xlsx)` | Lectura binaria ultraveloz de hojas de cálculo Yape en el cliente. |

---

## ⚙️ Instalación y Ejecución Local

Sigue estos sencillos pasos para correr el procesador localmente en tu computadora:

### Prerrequisitos
Tener instalado Node.js (versión 18+) y **pnpm** (recomendado):
```bash
npm install -g pnpm
```

### Pasos de Configuración

1. **Clonar el proyecto:**
   ```bash
   git clone https://github.com/JorgeZegarra22/Procesador-Yape-Excel.git
   cd Procesador-Yape-Excel
   ```

2. **Instalar dependencias:**
   ```bash
   pnpm install
   ```

3. **Correr en Modo Desarrollo:**
   ```bash
   pnpm run dev
   ```
   Abre [http://localhost:4321](http://localhost:4321) en tu navegador para ver la aplicación activa.

4. **Compilar para Producción:**
   ```bash
   pnpm run build
   ```

---

## 📜 Licencia
Este proyecto está bajo la licencia **MIT**. Puedes usarlo libremente para tus sorteos.

---
*Desarrollado por **Jorge Zegarra**.*

[astro-url]: https://astro.build/
[typescript-url]: https://www.typescriptlang.org/
[tailwind-url]: https://tailwindcss.com/
[license-url]: https://opensource.org/licenses/MIT

[astro-badge]: https://img.shields.io/badge/Astro-352563?style=for-the-badge&logo=astro&logoColor=FF7E33
[typescript-badge]: https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white
[tailwind-badge]: https://img.shields.io/badge/Tailwind_CSS-38BDF8?style=for-the-badge&logo=tailwindcss&logoColor=white
[license-badge]: https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge
