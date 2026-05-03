from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
import os

load_dotenv()

ACCOUNT_USER = os.getenv("ACCOUNT_USER")
ACCOUNT_PSWD = os.getenv("ACCOUNT_PSWD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, 10)

join_btn = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "Home_heroButton__3eeI3")))
join_btn.click()

email = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email.send_keys(ACCOUNT_USER)

password = wait.until(ec.presence_of_element_located((By.ID, "password-input")))
password.send_keys(ACCOUNT_PSWD)

login_btn = wait.until(ec.element_to_be_clickable((By.ID, "submit-button")))
login_btn.click()

wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='class-card-']")))

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

booked_classes = 0
waitlists_joined = 0
already_booked = 0

processed_classes = []

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            book_btn = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            class_info = f"{class_name} on {day_title}"

            if book_btn.text == "Booked":
                print(f"Already booked {class_info}")
                already_booked += 1
                processed_classes.append(f"[Booked] {class_info}")

            elif book_btn.text == "Book Class":
                book_btn.click()
                print(f"Booked: {class_info} for 6:00 PM")
                booked_classes += 1
                processed_classes.append(f"[New Booking] {class_info}")
            
            elif book_btn.text == "Join Waitlist":
                book_btn.click()
                print(f"Joined waitlist for {class_info}")
                waitlists_joined += 1
                processed_classes.append(f"[New Waitlist] {class_info}")

            elif book_btn.text == "Waitlisted":
                print(f"Already on waitlist for {class_info}")
                already_booked += 1
                processed_classes.append(f"[Waitlisted] {class_info}")

# print("\n--- BOOKING SUMMARY ---")
# print(f"Classes booked: {booked_classes}")
# print(f"Waitlists joined: {waitlists_joined}")
# print(f"Already booked/waitlisted: {already_booked}")
print(f"Total Tuesday and Thursday 6pm classes: {booked_classes + waitlists_joined + already_booked}")

# print("\n--- DETAILED CLASS LIST---")
# for class_detail in processed_classes:
#     print(class_detail)
total_booked = already_booked + booked_classes + waitlists_joined
print(f"\n--- VERIFYING ON MY BOOKINGS PAGE ---")

bookings_btn = driver.find_element(By.ID, "my-bookings-link")
bookings_btn.click()

wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

verified_count = 0

all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        pass

# Simple comparison
print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")