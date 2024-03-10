function toggleContent(header) {
    const content = header.nextElementSibling;
    content.classList.toggle('show');
    const arrow = header.querySelector('.arrow');
    arrow.textContent = content.classList.contains('show') ? '▲' : '▼';
}
