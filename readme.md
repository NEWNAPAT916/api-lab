# api-lab

API tests for QuickPizza with pytest and requests.

## Install and run

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

## Input domain model (Step A1)

| Characteristic | Blocks | Values in the tests |
|---|---|---|
| C1 Value of stars | below 1, 1 to 5 (base), above 5 | 0, 3, 6 |
| C2 Type of stars | whole number (base), decimal, text, missing | 3, 3.5, "3", no field |
| C3 Pizza | exists (base), does not exist | a new pizza, 999999999 |
| C4 Token | the user's own (base), none, wrong length | from auth, no header, token short |

## Test coverage of each block (Step A2)

| Block | Test |
|---|---|
| C1 below 1 | `test_stars_out_of_range[0]` |
| C1 1 to 5 (base) | `test_base_choice_is_saved` |
| C1 above 5 | `test_stars_out_of_range[6]` |
| C2 whole number (base) | `test_base_choice_is_saved` |
| C2 decimal | `test_stars_decimal_is_refused` |
| C2 text | `test_stars_text_is_refused` |
| C2 missing | `test_stars_missing_is_refused` |
| C3 exists (base) | `test_base_choice_is_saved` |
| C3 does not exist | `test_unknown_pizza_is_refused` |
| C4 own token (base) | `test_base_choice_is_saved` |
| C4 none | `test_no_token_is_refused` |
| C4 wrong length | `test_short_token_is_refused` |

## Part B

1. การทดสอบกับเซิร์ฟเวอร์จริงผ่านอินเทอร์เน็ตหาข้อผิดพลาดได้ เช่น ปัญหาเครือข่ายและการติดตั้งระบบ (ตัวอย่างคือ load balancer ส่งคำขอไปผิดเซิร์ฟเวอร์ หรือคำขอหมดเวลา) และข้อผิดพลาดในการทำงานร่วมกันของเว็บเซิร์ฟเวอร์ โค้ด และข้อมูลที่เก็บไว้ (ตัวอย่างคือ status code หรือรูปแบบ JSON ผิด) unit test ที่ใช้ stub ไม่เห็นข้อผิดพลาดเหล่านี้ เพราะ stub เข้าไปแทนส่วนเหล่านั้นแล้ว อย่างไรก็ตามยังควรเขียน unit test แบบใช้ stub ด้วย เพราะรันเร็ว ไม่ต้องใช้เครือข่าย ให้ผลเหมือนเดิมทุกครั้ง และชี้ได้ว่าฟังก์ชันไหนผิด

2. ถ้าใช้ token สาธารณะ ข้อมูลจะเป็นของทุกคนร่วมกัน คนอื่นอาจแก้ข้อมูลระหว่างที่เทสต์ของฉันรันอยู่ และฉันอาจไปทำข้อมูลของคนอื่นเสียหาย การสร้าง user ใหม่ในทุกเทสต์ทำให้แต่ละเทสต์มีข้อมูลของตัวเอง ผลจึงไม่ขึ้นกับเทสต์อื่นหรือคนอื่น ใน Project 2 ฉันจะสร้างข้อมูลของตัวเอง (เช่น สินค้า ตะกร้า ห้องพัก หรือการจอง) ภายในแต่ละเทสต์หรือ fixture ตั้งชื่อที่ไม่ซ้ำ ลบทิ้งเมื่อเทสต์จบ และไม่แตะข้อมูลของกลุ่มอื่น

3. session เก็บ cookie ที่เซิร์ฟเวอร์ส่งกลับมา รวมถึง AWSALB ซึ่ง load balancer ใช้ส่งทุกคำขอไปยังเซิร์ฟเวอร์เครื่องเดิม และเครื่องนั้นคือเครื่องที่รู้จัก user ที่ฉันเพิ่งสร้าง ถ้าไม่มี session การล็อกอินอาจไปถึงเซิร์ฟเวอร์ที่ไม่รู้จัก user นั้น แล้วล้มเหลวด้วย 401 ผลการรัน 3 ครั้งใน Step 0.12 ของฉันคือ: [pass, fail 401, fail 401] เทสต์นี้ผ่านบ้างล้มบ้างทั้งที่ไม่ได้แก้โค้ด จึงเป็นเทสต์ที่ไม่เสถียร (flaky)

4. block "exclude ครบทั้ง 3 tool" เป็นตัวที่เผยข้อบกพร่อง เพราะเซิร์ฟเวอร์ตอบ 500 การตอบ 500 พร้อม body ว่างแย่กว่า เพราะแอปไม่ได้ข้อมูลอะไรเลย ดูเหมือนเซิร์ฟเวอร์พัง และอาจทำให้แอปลองส่งซ้ำโดยไม่มีประโยชน์ ส่วน 400 พร้อมข้อความบอกแอปว่าอินพุตผิดและควรแก้อะไร เทสต์นี้ยังอยู่ในชุดเป็น xfail เพื่อให้ข้อบกพร่องถูกบันทึกและมองเห็นอยู่ ขณะที่เทสต์อื่นยังเป็นสีเขียว และเมื่อใช้ strict=True ถ้า QuickPizza แก้ข้อบกพร่องแล้ว การรันจะล้มเพื่อเตือนให้ฉันเอาเครื่องหมาย xfail ออก

5. base choice coverage ต้องใช้ 1 + (3 - 1) + (4 - 1) + (2 - 1) + (3 - 1) = 1 + 2 + 3 + 1 + 2 = 9 เทสต์ ส่วน all combinations coverage ต้องใช้ 3 x 4 x 2 x 3 = 72 เทสต์

6. อ่านได้ 404, แก้ได้ 400 และลบได้ 400 ฉันคาดว่าจะได้ 403 Forbidden (รู้ว่าเป็นใครแต่ไม่มีสิทธิ์) หรือ 404 ทั้งสามกรณีเพื่อซ่อนว่า rating นี้มีอยู่จริง rating ไม่เปลี่ยนในทุกกรณี การควบคุมสิทธิ์จึงทำงานถูกต้อง และไม่ใช่ช่องโหว่ด้านความปลอดภัย แต่รหัสไม่สอดคล้องกัน และ 400 ไม่ตรงกับสาเหตุจริงซึ่งคือเรื่องความเป็นเจ้าของ จึงเป็นข้อบกพร่องเล็กน้อยในการรายงานข้อผิดพลาด

7. เซิร์ฟเวอร์ตอบ 401 พร้อม {"error":"authentication failed"} ไม่ถือเป็นข้อบกพร่อง เพราะ token ปลอมไม่ผูกกับ user ใดเลย API จึงปฏิเสธซึ่งเป็นพฤติกรรมที่ถูกต้อง ถ้า API ยอมรับและส่ง ratings กลับมา คนแปลกหน้าจะเดา token แล้วอ่าน แก้ หรือลบข้อมูลของผู้ใช้จริงได้โดยไม่ต้องล็อกอิน ซึ่งจะเป็นข้อบกพร่องด้านความปลอดภัยที่ร้ายแรง

8. API test ตรวจสิ่งเหล่านี้ได้ดีกว่า: status code ข้อความ error ฟิลด์ JSON และอินพุตแปลกๆ และรันเร็วกว่า ส่วนการทดสอบผ่านหน้าเว็บเท่านั้นที่ตรวจได้ว่าผู้ใช้เห็นและทำอะไรได้จริง เช่น หน้าตา ปุ่ม การทำงานของ JavaScript และหน้าเว็บแสดงข้อมูลถูกต้องหรือไม่