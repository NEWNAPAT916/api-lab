# api-lab
 {"names":["Americana","Bolognese","Calzone","Capricciosa","Carbonara","Frut
                    ti di Mare","Funghi","Fungi e Olive","Hawaii","Margherita","Marinara","Napo
                    letana","Prosciutto","Pugliese","Quattro Formaggi"...

Set-Cookie: AWSALB=/MRO0my2Lw2QgHuZvAFaEn57g5CX7oLJ73BILEmkNYxB5diwnO56bAPyT9JtH6dkTxHXMK3K2wu+GT/uWL8ZUXxtYwZOjTzFR3BPWiKLeR7RAX3uGWuOLAJC+AOG

HTTP/1.1 401 Unauthorized

{"pizza":{"id":120462,"name":"A True Siciliana","dough":{"ID":1,"name":"Thin","caloriesPerSlice":100},"ingredients":[{"ID":35,"name":"Asparagus","caloriesPerSlice":50,"vegetarian":true},{"ID":14,"name":"Extra cheese","caloriesPerSlice":100,"vegetarian":true},{"ID":2,"name":"Olive oil","caloriesPerSlice":100,"vegetarian":true},{"ID":4,"name":"Bianco di Nizza tomatoes","caloriesPerSlice":50,"vegetarian":true},{"ID":8,"name":"Mozzarella fior di latte","caloriesPerSlice":150,"vegetarian":true},{"ID":11,"name":"Onions","caloriesPerSlice":50,"vegetarian":true},{"ID":19,"name":"Garlic","caloriesPerSlice":25,"vegetarian":true}],"tool":"Pizza cutter"},"calories":525,"vegetarian":true}

step 12 รัน pytest -v test_no_session.py 3 ครั้ง 
1. 1 passed in 2.21s 
2. 1 failed in 2.18s
3. 1 failed in 2.21s

| Block | ตัวอย่าง input |
|---|---|
| ไม่ exclude เลย (0 tools) | `[]` |
| exclude 1 ชิ้น (1 tool) | `["Knife"]`, `["Scissors"]` (มีแล้ว) |
| exclude 2 ชิ้น (2 tools) | `["Knife", "Scissors"]` |
| exclude ทั้ง 3 ชิ้น (3 tools) | `["Knife", "Pizza cutter", "Scissors"]` |

## Defect report

- Title: POST /api/pizza answers 500 with an empty body when all three tools are excluded
- Request: `POST https://quickpizza.grafana.com/api/pizza` with header `Authorization: token <token>` and body `{"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}`
- Expected result: status 400 and a JSON error message, because no pizza can be cut without a tool
- Actual result: status 500 Internal Server Error with an empty body
- Severity: Medium. The failure repeats on every request with this input, and the caller gets no message that says what was wrong. No data is lost.