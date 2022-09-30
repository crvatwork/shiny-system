from playwright.sync_api import Playwright, sync_playwright, expect
from PIL import Image, ImageDraw

class ImageMarkup:
    def __init__(self, filename: str, color: str = '#ff0000') -> None:
        self.filename = filename
        self.color: str = color
        self.image = Image.open(self.filename)
        self.drawing = ImageDraw.Draw(self.image)

    def add_box(self, coords: list, width: int = 2):
        self.drawing.rectangle(coords, width=width, outline=self.color)

    def write_image(self):
        self.image.save('annotated_' + self.filename)

    def show_image(self):
        self.image.show()

def boxit(imgfile):
    mark = ImageMarkup(filename=imgfile)
    box = [243, 239, 291, 258]
    mark.add_box(coords=box)
    mark.write_image()

def run(playwright: Playwright, imgfile: str) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    page = context.new_page()

    # Go to https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&t=seti&wt=none&l=application%2Fx-sh&width=680&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=1x&wm=false&code=%2523%21%252Fbin%252Fbash%250Aecho%2520%2522Show%2520me%2520where%2520my%2520home%2520directory%2520lives%2522%250Aecho%2520%2524HOME%250Aecho%2520%2522Show%2520me%2520who%2520I%2520am%2520logged%2520in%2520as%2522%250Aecho%2520%2524USER%250A%2523%2520Can%2520you%2520find%2520the%2520typo%253F%250A%2523%2520-----------------------------%250Aecho%2520%2522Tell%2520me%2520what%2520is%2520worng%2520with%2520this%2520line%2520of%2520text%2522
    page.goto("https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&t=seti&wt=none&l=application%2Fx-sh&width=680&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=1x&wm=false&code=%2523%21%252Fbin%252Fbash%250Aecho%2520%2522Show%2520me%2520where%2520my%2520home%2520directory%2520lives%2522%250Aecho%2520%2524HOME%250Aecho%2520%2522Show%2520me%2520who%2520I%2520am%2520logged%2520in%2520as%2522%250Aecho%2520%2524USER%250A%2523%2520Can%2520you%2520find%2520the%2520typo%253F%250A%2523%2520-----------------------------%250Aecho%2520%2522Tell%2520me%2520what%2520is%2520worng%2520with%2520this%2520line%2520of%2520text%2522")

    # Click button:has-text("Export menu dropdown")
    page.locator("button:has-text(\"Export menu dropdown\")").click()
    page.wait_for_url("https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&t=seti&wt=none&l=application%2Fx-sh&width=680&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=1x&wm=false&code=%2523%21%252Fbin%252Fbash%250Aecho%2520%2522Show%2520me%2520where%2520my%2520home%2520directory%2520lives%2522%250Aecho%2520%2524HOME%250Aecho%2520%2522Show%2520me%2520who%2520I%2520am%2520logged%2520in%2520as%2522%250Aecho%2520%2524USER%250A%2523%2520Can%2520you%2520find%2520the%2520typo%253F%250A%2523%2520-----------------------------%250Aecho%2520%2522Tell%2520me%2520what%2520is%2520worng%2520with%2520this%2520line%2520of%2520text%2522")

    # Click text=1x
    page.locator("text=1x").click()
    page.wait_for_url("https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&t=seti&wt=none&l=application%2Fx-sh&width=680&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=1x&wm=false&code=%2523%21%252Fbin%252Fbash%250Aecho%2520%2522Show%2520me%2520where%2520my%2520home%2520directory%2520lives%2522%250Aecho%2520%2524HOME%250Aecho%2520%2522Show%2520me%2520who%2520I%2520am%2520logged%2520in%2520as%2522%250Aecho%2520%2524USER%250A%2523%2520Can%2520you%2520find%2520the%2520typo%253F%250A%2523%2520-----------------------------%250Aecho%2520%2522Tell%2520me%2520what%2520is%2520worng%2520with%2520this%2520line%2520of%2520text%2522")

    # Start waiting for the download
    with page.expect_download() as download_info:
        # Perform the action that initiates download
        page.locator("text=PNG").click()
    download = download_info.value
    # Wait for the download process to complete
    # Save downloaded file somewhere
    download.save_as(imgfile)

    context.close()
    browser.close()

def main():
    image_name = 'carbon.png'
    with sync_playwright() as playwright:
        run(playwright, image_name)
    boxit(image_name)

if __name__ == "__main__":
    main()