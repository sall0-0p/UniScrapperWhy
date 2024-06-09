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
};