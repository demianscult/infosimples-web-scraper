# Bibliotecas instalada manualmente
from bs4 import BeautifulSoup
import requests
# Bibliotecas nativas do Python
import json

# URL do site
url = 'https://infosimples.com/vagas/desafio/commercia/product.html'

# Objeto contendo a resposta final
resposta_final = {
    "title": None,
    "brand": None,
    "categories": [],
    "description": None,
    "skus": [],
    "properties": [],
    "reviews": [],
    "reviews_average_score": None,
    "url": url
}

try:
    # Faz o request de contéudo da página
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = 'utf-8'
    parsed_html = BeautifulSoup(response.content, 'html.parser')

    # Coleta título do Produto
    title_element = parsed_html.select_one('h2#product_title')
    resposta_final['title'] = title_element.get_text().strip() if title_element else None

    # Coleta a Marca
    brand_element = parsed_html.select_one('div[itemprop="brand"] meta[itemprop="name"]')
    resposta_final['brand'] = brand_element['content'].strip() if brand_element and 'content' in brand_element.attrs else None

    # Coleta a Descrição dos produtos
    description_meta = parsed_html.select_one('meta[itemprop="description"]')
    resposta_final['description'] = description_meta['content'].strip() if description_meta and 'content' in description_meta.attrs else None

    # SKUs para encontrar todas as variações e seus detalhes
    skus_data = []
    skus_area = parsed_html.select_one('.skus-area')
    if skus_area:
        product_cards = skus_area.select('.card')
        for card in product_cards:
            name_meta = card.select_one('meta[itemprop="name"]')
            sku_meta = card.select_one('meta[itemprop="sku"]')
            price_now_element = card.select_one('.prod-pnow')
            price_old_element = card.select_one('.prod-pold')
            availability_class = card.get('class', [])

            name = name_meta['content'].strip() if name_meta and 'content' in name_meta.attrs else None
            sku = sku_meta['content'].strip() if sku_meta and 'content' in sku_meta.attrs else None

            price_now_text = price_now_element.get_text().replace('R$', '').strip().replace(',', '.') if price_now_element else None
            current_price = float(price_now_text) if price_now_text else None

            price_old_text = price_old_element.get_text().replace('R$', '').strip().replace(',', '.') if price_old_element else None
            old_price = float(price_old_text) if price_old_text else None

            available = True if 'not-avaliable' not in availability_class else False

            skus_data.append({
                "name": name,
                "current_price": current_price,
                "old_price": old_price,
                "available": available,
                "sku": sku
            })
    resposta_final['skus'] = skus_data

   # Propriedades
    properties_data = []

    # Extrair propriedades da tabela "Product properties"
    product_properties_section = parsed_html.select_one('div:has(h4:contains("Product properties"))')
    if product_properties_section:
        product_properties_table = product_properties_section.select_one('table.pure-table.pure-table-bordered tbody')
        if product_properties_table:
            rows = product_properties_table.select('tr')
            for row in rows:
                cols = row.select('td')
                if len(cols) == 2:
                    label_element = cols[0].select_one('b')
                    label = label_element.get_text().strip() if label_element else cols[0].get_text().strip()
                    value = cols[1].get_text().strip()
                    properties_data.append({"label": label, "value": value})

    resposta_final['properties'] = properties_data

# Reviews e average score
    reviews_data = []
    comments_section = parsed_html.select_one('#comments')
    average_score = None

    if comments_section:
        average_score_element = comments_section.select_one('h4:contains("Average score:")')
        if average_score_element:
            score_text = average_score_element.get_text().split(':')[-1].strip().split('/')[0].strip()
            try:
                average_score = float(score_text)
            except ValueError:
                average_score = None

        review_boxes = comments_section.select('.analisebox')
        for review_box in review_boxes:
            username_element = review_box.select_one('.analiseusername')
            date_element = review_box.select_one('.analisedate')
            stars_element = review_box.select_one('.analisestars')
            text_element = review_box.select_one('p')

            name = username_element.get_text().strip() if username_element else None
            date = date_element.get_text().strip() if date_element else None
            text = text_element.get_text().strip() if text_element else None

            score = 0
            if stars_element:
                score = stars_element.get_text().count('★') # Conta o número de estrelas preenchidas

            reviews_data.append({"name": name, "date": date, "score": score, "text": text})

    resposta_final['reviews'] = reviews_data
    resposta_final['reviews_average_score'] = average_score

    # Categorias
    categories_elements = parsed_html.select('.breadcrumb li a')
    categories = [cat.get_text().strip() for cat in categories_elements]
    resposta_final['categories'] = categories

    # Gera string JSON com a resposta final
    json_resposta_final = json.dumps(resposta_final, indent=4, ensure_ascii=False)

    # Salva o arquivo JSON com a resposta final
    with open('produto.json', 'w', encoding='utf-8') as arquivo_json:
        arquivo_json.write(json_resposta_final + '\n')

    print("Dados extraídos e salvos em produto.json com sucesso!")

except requests.exceptions.RequestException as e:
    print(f"Erro na requisição HTTP: {e}")
except AttributeError as e:
    print(f"Erro ao extrair dados do HTML: {e}")
except ValueError as e:
    print(f"Erro ao converter valor: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")