export default class BaseModel {
  baseUrl = '';

  constructor(apiUrl) {
    this.baseUrl = apiUrl;
  }

  create(post) {
    return fetch(this.baseUrl, {
      method: 'post',
      body: JSON.stringify(post),
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    }).then(res => res.json());
  }

  remove(id) {
    return fetch(`${this.baseUrl}/${id}`, {
      method: 'delete',
    }).then(res => res.json());
  }
}