from bs4 import BeautifulSoup as bs
import requests

def download_file(url, filename):
  with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(filename.replace('HSK标准教程','HSK_'), 'wb') as f:
      for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)
    print(f"Downloaded {filename}")
  return filename

def download_files_from_list(links, class_filter):
  for link in links:
    download_link, title = get_links_from_website(link, class_filter)
    download_file(download_link[0], f"{title}.mp3")

def get_links_from_website(site, class_filter):
  site_base = "/".join(site.split("/")[0:3])
  response = requests.get(site)
  soup = bs(response.content, 'html.parser')
  html_links = soup.find_all("a", class_=class_filter)
  return [site_base+"/"+link['href'] for link in html_links], soup.find('title').string

def process_hsk_resource_page(url):
  links, _=get_links_from_website(url, "list-group-item")
  download_files_from_list(links, "down_btn theme_b")

process_hsk_resource_page("http://www.blcup.com/MobileResSeries?rid=1cd84d66-f817-40a4-bfaf-2d58b02ebe3a")
process_hsk_resource_page("http://www.blcup.com/MobileResSeries?rid=040d3754-5e4e-4e75-8640-be9b29289493")
process_hsk_resource_page("http://www.blcup.com/MobileResSeries?rid=899d602d-177e-4fb9-bc7f-c7f13b8b6519")
process_hsk_resource_page("http://www.blcup.com/MobileResource?rid=d82202ec-f281-4a00-924d-78c5419428b6")
process_hsk_resource_page("http://www.blcup.com/MobileResSeries?rid=4c545205-cd03-4496-9576-7ad165099c7c")
process_hsk_resource_page("http://www.blcup.com/MobileResSeries?rid=c55419ff-dd4c-4ead-9dae-0d159197f622")
