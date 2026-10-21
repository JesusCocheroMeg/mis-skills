---
name: "reporte-daily"
description: "Genera el reporte diario del daily de Jesus (Hoy estoy en / Me frena / Necesito a), resumido y en lenguaje no técnico, a partir de lo que cuente o del contexto de la conversación actual."
---

# Reporte Daily

Genera el reporte diario del daily con lo que Jesus está trabajando hoy. Suele llevar varios proyectos a la vez.

## Cuándo usarla

- Cuando pida "el daily", "reporte del día", "mi standup" o algo parecido.
- Cuando la invoque en medio de otra conversación: en ese caso saca el contexto de lo que se ha trabajado en ESA conversación (archivos, código, bugs, documentos, proyectos mencionados) y arma el reporte con eso.

## Fuentes de información (en este orden)

1. Lo que Jesus escriba en el mensaje (notas sueltas, lista desordenada, audio transcrito, etc.).
2. El contexto de la conversación actual: qué se hizo, qué proyecto, qué se corrigió o desplegó.
3. Si algo de "Me frena" o "Necesito a" no está claro, NO inventes: usa "de momento nada." en Me frena, y en Necesito a pon "de momento nadie." o pregunta una sola vez si parece que sí depende de alguien.

## Reglas de redacción

- MUY resumido: cada punto en 1 o 2 líneas como máximo.
- Entendible para personas no técnicas: di QUÉ se hace y PARA QUÉ sirve ("para mejor funcionamiento de la plataforma", "para que los pagos funcionen bien dentro de HERMES"). Evita jerga; si un término técnico es inevitable (ADR, worker, iframe), déjalo pero acompáñalo del beneficio.
- Mantén los nombres de proyectos, plataformas y personas tal como los usa Jesus (Megpay, HERMES, speechanalytics, Docmost, Nova, Enigma, CRMs, etc.).
- Si una tarea la adaptó o la empezó otra persona, menciónalo entre paréntesis: "( adaptado por Yeferson )".
- Agrupa tareas del mismo proyecto en un solo punto.
- Fecha de hoy en formato DD/MM/AAAA.
- Español, sin emojis, sin explicaciones extra antes o después: solo el reporte, listo para copiar y pegar (WhatsApp, Slack o Teams).

## Formato exacto de salida

```
Reporte DD/MM/AAAA

Hoy estoy en:

* <tarea 1 resumida + para qué sirve>.
* <tarea 2 resumida + para qué sirve>.

Me frena: <bloqueo o "de momento nada.">

Necesito a: <persona + para qué, o "de momento nadie.">
```

## Ejemplo

```
Reporte 19/10/2026

Hoy estoy en:

* Despliegue y solución de bugs del worker de transcripciones y evaluaciones de Speechanalytics, para un mejor funcionamiento de la plataforma ( adaptado por Yeferson ).
* Corrección de ADR's en Megpay, principalmente el ADR-015 documentado en Docmost, para que los iframes funcionen mejor en HERMES.

Me frena: de momento nada.

Necesito a: Juliana para el testeo del iframe de la pasarela de pagos.
```

Entrega el reporte en un bloque de código para que sea fácil de copiar. Si Jesus pide ajustes ("quita esto", "agrega que..."), devuelve el reporte completo actualizado.