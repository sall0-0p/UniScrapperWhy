import BaseRepository from '../BaseRepository';

export default class ProductRepository extends BaseRepository {
  getProductList(onlyMeta) {
    if (onlyMeta) {
      return fetch(`${this.baseUrl}/product-meta`, { method: 'get' }).then(res => res.json());
    } else {
      return fetch(`${this.baseUrl}/products`, { method: 'get'}).then(res => res.json());
    };
  };

  getProductData(productId) {
    return fetch(`${this.baseUrl}/product/${productId}`, { method: 'get' });
  }

  getNewProduct(productId) {
    return fetch(`${this.baseUrl}/product/${productId}`, { method: 'get' });
  }

  refreshProduct(productId) {
    return fetch(`${this.baseUrl}/product/${productId}`, { method: 'post' });
  };

  deleteProduct(productId) {
    return fetch(`${this.baseUrl}/product/${productId}`, { method: 'delete' });
  };

  clearProductList() {
    return fetch(`${this.baseUrl}/products`, { method: 'delete' });
  };

  async downloadProduct(productId, type) {
    const response = await fetch(`${this.baseUrl}/download/${productId}/${type}`)

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `${productId}.${type.toLowerCase()}`); // Update this with the actual file name
    document.body.appendChild(link);
    link.click();
    link.remove();
  };
};