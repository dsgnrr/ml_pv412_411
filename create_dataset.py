import os
from icrawler.builtin import BaiduImageCrawler

def download_data(search_queries:dict):
    max_images_per_query = 15
    
    for folder_name, query_text in search_queries.items():
        
        output_directory = f"./dataset/{folder_name}"
        
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        crawler = BaiduImageCrawler(downloader_threads=4, storage={'root_dir':output_directory})
        crawler.crawl(keyword=query_text, max_num=max_images_per_query)
    
        for i, filename in enumerate(os.listdir(output_directory), start=1):
            old_path = os.path.join(output_directory, filename)
            new_path = os.path.join(output_directory, f"{folder_name}_{i}.jpg")
            os.rename(old_path, new_path)

# folder_name => query     
search_queries = {
    # "anime": "Cyberpunk Edgerunners",
    "dog": "German Shepherd",
    # "cat": "кішка",
    # "cartoon":"Tom and Jerry"
}

if __name__ == "__main__":
    download_data(search_queries)