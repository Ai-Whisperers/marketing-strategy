# Hosting Costs Guide - AI Whisperers

> **Ultima actualizacion**: Enero 2025
> **Proposito**: Referencia de costos reales de hosting para proyectos SaaS
> **Herramientas principales**: Vercel + Supabase

---

## 1. VERCEL - Frontend & Serverless

### Planes Disponibles

| Plan | Costo | Uso permitido |
|------|-------|---------------|
| **Hobby** | GRATIS | Solo personal, NO comercial |
| **Pro** | $20/usuario/mes | Comercial, equipos |
| **Enterprise** | Custom | Grandes empresas |

### Vercel Hobby (Gratis) - Limites

| Recurso | Limite |
|---------|--------|
| Proyectos | Ilimitados (max 200) |
| Bandwidth | 100 GB/mes |
| Serverless Functions | 150,000 invocaciones/mes |
| Functions por deploy | 12 max |
| Build minutes | 100 horas/mes |
| **USO** | **Solo personal, NO comercial** |

**IMPORTANTE**: El plan Hobby NO se puede usar para proyectos comerciales como VetePy.

### Vercel Pro ($20/usuario/mes) - Incluye

| Recurso | Incluido |
|---------|----------|
| Credito mensual | $20 flexible |
| Fast Data Transfer | $150+ incluido |
| Edge Requests | $20+ incluido |
| Proyectos | Ilimitados |
| Team members (viewers) | GRATIS |
| Bandwidth | 1 TB/mes base |

### Vercel - Costos de Overage (si excedes)

| Recurso | Costo extra |
|---------|-------------|
| Bandwidth | $0.15/GB despues de 1TB |
| Serverless compute | Variable segun uso |
| Edge functions | Variable segun uso |

---

## 2. SUPABASE - Backend & Database

### Planes Disponibles

| Plan | Costo | Proyectos |
|------|-------|-----------|
| **Free** | GRATIS | 2 proyectos activos |
| **Pro** | $25/mes/proyecto | Ilimitados |
| **Team** | $599/mes | Ilimitados + features |
| **Enterprise** | Custom | Custom |

### Supabase Free - Limites (por proyecto)

| Recurso | Limite |
|---------|--------|
| Proyectos activos | 2 max |
| Database size | 500 MB |
| File storage | 1 GB |
| Bandwidth | 5 GB/mes |
| MAUs (usuarios) | 50,000 |
| Edge Functions | 500,000 calls/mes |
| Realtime connections | 200 concurrent |
| **Pausa por inactividad** | 1 semana sin uso |

### Supabase Pro ($25/mes/proyecto) - Incluye

| Recurso | Incluido |
|---------|----------|
| Database size | 8 GB |
| File storage | 100 GB |
| MAUs | 100,000 |
| Compute credits | $10/mes |
| Pausa automatica | NO (siempre activo) |
| Backups diarios | Si |

### Supabase - Costos de Overage

| Recurso | Costo extra |
|---------|-------------|
| Storage | $0.021/GB/mes |
| Database egress | $0.09/GB |
| MAUs extras | $0.00325/MAU |
| Compute extra | Variable |

---

## 3. COSTO REAL POR PROYECTO COMERCIAL

### Escenario: 1 Proyecto SaaS (ej. VetePy)

| Servicio | Plan | Costo/mes USD |
|----------|------|---------------|
| Vercel Pro | 1 usuario | $20 |
| Supabase Pro | 1 proyecto | $25 |
| **TOTAL** | | **$45/mes** |

### Escenario: Multi-tenant SaaS (muchos clientes, 1 proyecto)

VetePy usa arquitectura multi-tenant: 1 proyecto de Supabase para TODOS los clientes.

| Servicio | Plan | Costo/mes USD |
|----------|------|---------------|
| Vercel Pro | 1 usuario | $20 |
| Supabase Pro | 1 proyecto | $25 |
| Storage extra (estimado) | +10GB | ~$0.21 |
| **TOTAL base** | | **~$45-50/mes** |

### Escenario: Multiples Proyectos Independientes

| Cantidad proyectos | Vercel | Supabase | Total/mes |
|--------------------|--------|----------|-----------|
| 1 proyecto | $20 | $25 | $45 |
| 2 proyectos | $20 | $50 | $70 |
| 3 proyectos | $20 | $75 | $95 |
| 5 proyectos | $20 | $125 | $145 |
| 10 proyectos | $20 | $250 | $270 |

**Nota**: Vercel cobra por usuario, no por proyecto. Supabase cobra por proyecto.

---

## 4. CONVERSION A GUARANIES

Cotizacion referencia: 1 USD = Gs. 7,500

| Costo USD | Costo Gs. |
|-----------|-----------|
| $20 | Gs. 150,000 |
| $25 | Gs. 187,500 |
| $45 | Gs. 337,500 |
| $50 | Gs. 375,000 |
| $70 | Gs. 525,000 |
| $100 | Gs. 750,000 |

---

## 5. APLICACION A VETEPY

### Estructura Actual

VetePy es **multi-tenant**: Un solo proyecto sirve a multiples veterinarias.

| Componente | Costo |
|------------|-------|
| Vercel Pro (1 dev) | $20/mes |
| Supabase Pro (1 proyecto) | $25/mes |
| **Costo fijo mensual** | **$45/mes (~Gs. 337,500)** |

### Costo por Cliente VetePy

| Cantidad clientes | Costo total | Costo por cliente |
|-------------------|-------------|-------------------|
| 1 cliente | $45 | $45.00 |
| 5 clientes | $45 | $9.00 |
| 10 clientes | $50 (estimado) | $5.00 |
| 20 clientes | $55 (estimado) | $2.75 |
| 50 clientes | $70 (estimado) | $1.40 |
| 100 clientes | $100 (estimado) | $1.00 |

**Economia de escala**: Mientras mas clientes, menor costo por cliente.

### Margen con Precio Actual (Gs. 250,000/mes = ~$33)

| Clientes | Ingreso total | Costo hosting | Margen |
|----------|---------------|---------------|--------|
| 1 | $33 | $45 | -$12 (perdida) |
| 2 | $66 | $45 | +$21 |
| 5 | $165 | $50 | +$115 |
| 10 | $330 | $55 | +$275 |
| 20 | $660 | $65 | +$595 |
| 50 | $1,650 | $100 | +$1,550 |

**Breakeven**: 2 clientes minimo para cubrir costos de hosting.

---

## 6. PRECIO DE HOSTING PARA COBRAR AL CLIENTE

### Opcion A: Hosting Incluido (actual)

Precio VetePy: Gs. 250,000/mes (hosting incluido)

| Pros | Contras |
|------|---------|
| Simple de vender | Menor margen con pocos clientes |
| Sin sorpresas para cliente | Subsidias hosting al inicio |
| Competitivo | |

### Opcion B: Hosting Separado

| Concepto | Precio sugerido |
|----------|-----------------|
| Servicio VetePy | Gs. 200,000/mes |
| Hosting | Gs. 50,000/mes |
| **Total** | Gs. 250,000/mes |

| Pros | Contras |
|------|---------|
| Transparencia | Mas complejo de explicar |
| Cliente entiende costos | Puede parecer "caro" desglosado |

### Opcion C: Hosting como Cargo Anual

| Concepto | Precio |
|----------|--------|
| Setup + Hosting anual | Gs. 500,000 (pago unico) |
| Servicio mensual | Gs. 200,000/mes |

**Nota**: Esta opcion garantiza al menos Gs. 500,000 upfront.

---

## 7. LISTA DE PRECIOS DE HOSTING (Para cualquier proyecto)

### Hosting Basico (sitio estatico, poco trafico)

| Servicio | Costo real | Precio sugerido cliente |
|----------|------------|-------------------------|
| Vercel Hobby | GRATIS | N/A (no comercial) |
| Vercel Pro basico | $20/mes | Gs. 200,000/mes |

### Hosting Estandar (SaaS, trafico moderado)

| Servicio | Costo real | Precio sugerido cliente |
|----------|------------|-------------------------|
| Vercel Pro | $20/mes | |
| Supabase Pro | $25/mes | |
| **Total** | $45/mes | **Gs. 400,000-500,000/mes** |

### Hosting Premium (alto trafico, mucho storage)

| Servicio | Costo real | Precio sugerido cliente |
|----------|------------|-------------------------|
| Vercel Pro + overages | $50-100/mes | |
| Supabase Pro + overages | $50-100/mes | |
| **Total** | $100-200/mes | **Gs. 900,000-1,500,000/mes** |

---

## 8. RECOMENDACION PARA VETEPY

### Mantener hosting incluido en el precio

**Razon**:
1. Gs. 250,000 ya es competitivo
2. Simplifica la venta
3. Con 2+ clientes ya cubris costos
4. La arquitectura multi-tenant escala bien

### Si queres separar hosting en el futuro:

| Plan | Servicio | Hosting | Total |
|------|----------|---------|-------|
| Basico | Gs. 100,000 | Gs. 50,000 | Gs. 150,000 |
| Profesional | Gs. 200,000 | Gs. 50,000 | Gs. 250,000 |
| Premium | Gs. 350,000 | Gs. 50,000 | Gs. 400,000 |

---

## FUENTES

- [Vercel Pricing](https://vercel.com/pricing)
- [Vercel Pro Plan Docs](https://vercel.com/docs/plans/pro-plan)
- [Vercel Hobby Plan Docs](https://vercel.com/docs/plans/hobby)
- [Vercel Pricing Breakdown - Flexprice](https://flexprice.io/blog/vercel-pricing-breakdown)
- [Supabase Pricing](https://supabase.com/pricing)
- [Supabase Billing Docs](https://supabase.com/docs/guides/platform/billing-on-supabase)
- [Supabase Pricing Breakdown - UI Bakery](https://uibakery.io/blog/supabase-pricing)
- [Supabase True Cost - MetaCTO](https://www.metacto.com/blogs/the-true-cost-of-supabase-a-comprehensive-guide-to-pricing-integration-and-maintenance)
