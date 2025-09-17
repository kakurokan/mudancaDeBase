# Conversor de Bases Numéricas (2–62)

Este projeto é um utilitário em **Python** que permite converter números entre diferentes bases, variando de **2** a **62**, com suporte a inteiros, frações, sinais negativos e separadores decimais (`.` e `,`).

---

## 🚀 Funcionalidades

- Conversão de números inteiros e fracionários entre qualquer base de 2 a 62.  
- Suporte a **sinais negativos** (`-`).  
- Aceita separadores decimais `.` e `,`.  
- Utiliza os dígitos:  
```

0-9  → valores 0–9
A-Z  → valores 10–35
a-z  → valores 36–61

````
- Limite de até **8 casas decimais** para evitar loops infinitos em frações periódicas.  
- Interface **interativa** no terminal.  

---

## 📦 Como usar

1. Tenha o **Python 3** instalado em sua máquina.
2. Baixe ou clone este repositório.
3. Execute o programa no terminal:

```bash
python3 conversor_bases.py
````

4. Digite:

   * O número que deseja converter.
   * A base do número inserido (2–62).
   * A base de destino (2–62).

---

## ⚙️ Estrutura do código

* `para_decimal_inteiro` → converte parte inteira para decimal.
* `para_decimal_fracionario` → converte parte fracionária para decimal.
* `decimal_base_inteiro` → converte inteiro decimal para base final.
* `decimal_base_fracionario` → converte fração decimal para base final.
* `base_para_base` → rotina principal de conversão.
* `main` → interface interativa no terminal.

---

## ⚠️ Limitações

* Precisão da fração limitada a **8 dígitos**.
* Conversão fracionária baseada em ponto flutuante (`float`).
* Não há suporte a prefixos (`0x`, `0b`, `0o`).

---

## 📄 Licença

Este projeto é de uso livre. Você pode copiar, modificar e distribuir como quiser.
Sugestão: incluir uma licença aberta, como **MIT** ou **GPLv3**.

---
