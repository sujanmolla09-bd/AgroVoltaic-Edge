# AgroVoltaic-Edge 🌿☀️

> **Autonomous Physical AI Microgrid & Edge-IoT Agent**  
> Powered by **NVIDIA Nemotron** via **Nebius Token Factory**, **Tavily Search API**, and **FastAPI**.

---

## 📌 Executive Summary

**AgroVoltaic-Edge** is an autonomous Physical AI framework designed to optimize dual-land use for solar power generation and precision agriculture. By marrying real-time edge telemetry with large language model reasoning (NVIDIA Nemotron via Nebius), the system independently orchestrates irrigation schedules, panel tilt angles, and microgrid cooling to prevent thermal loss and maximize crop yield.

---

## 🏗 System Architecture

```text
  [ Field IoT Telemetry ] ──> [ FastAPI Gateway ] ──> [ NVIDIA Nemotron (Nebius) ]
  (Sensors/Soil/Panels)            │                            │
                                   ▼                            ▼
                          [ Tavily Search API ] ──> [ Autonomous Decision Engine ]
                            (Live Weather Data)                 │
                                                                ▼
                                                    [ Physical Hardware Action ]
                                                    (Pump Control / Tilt Motor)
