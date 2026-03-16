# AI Research Agent

Agente en Python que investiga cualquier tema automáticamente usando GPT-4o-mini. Busca en la web y en Wikipedia, resume la información y la guarda en un archivo.

## Cómo funciona

Ejecutas `main.py`, escribes un tema y el agente se encarga de buscarlo, resumirlo y guardarlo en `research_output.txt`.



## Instalación

```bash
git clone https://github.com/TU-USUARIO/ai-research-agent.git
cd ai-research-agent
pip install -r requirements.txt
```

Crea un archivo `.env` con tu API key de OpenAI:

```
OPENAI_API_KEY=tu_clave
```

## Uso

```bash
python main.py
```

## Dependencias principales

- LangChain
- OpenAI
- DuckDuckGo Search
- Wikipedia
- Pydantic
