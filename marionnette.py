from marionette_driver.marionette import Marionette
from marionette_driver import By
client = Marionette('localhost', port=2828)
client.start_session()
client.get_url()
client.find_element(By.TAG_NAME,'body')
