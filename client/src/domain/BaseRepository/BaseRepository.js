export default class BaseRepository {
  baseUrl = '';

  constructor(apiUrl) {
    this.baseUrl = apiUrl;
  }

  fetch() {
      return fetch(this.baseUrl, { method: 'get' }).then(res => res.json());
  }
}