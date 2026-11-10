class HTMLGen {
  constructor() { }
  
  a(textContent) {
    return `<a>${textContent}</a>`;
  }
  
  b(textContent) {
    return `<b>${textContent}</b>`;
  }
  
  p(textContent) {
    return `<p>${textContent}</p>`;
  }
  
  body(textContent) {
    return `<body>${textContent}</body>`;
  }
  
  div(textContent) {
    return `<div>${textContent}</div>`;
  }
  
  span(textContent) {
    return `<span>${textContent}</span>`;
  }
  
  title(textContent) {
    return `<title>${textContent}</title>`;
  }
  
  comment(textContent) {
    return `<!--${textContent}-->`;
  }
}