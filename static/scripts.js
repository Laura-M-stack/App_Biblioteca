// Editar libro
document.getElementById('formulario-editar-libro').addEventListener('submit', (e) => {
    e.preventDefault();
    const id_libro = document.getElementById('id_libro').value;
    const nuevo_titulo = document.getElementById('nuevo_titulo').value;
    const nuevo_autor = document.getElementById('nuevo_autor').value;
    const nueva_editorial = document.getElementById('nueva_editorial').value;
    fetch('/editar-libro', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id_libro, nuevo_titulo, nuevo_autor, nueva_editorial })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
  });
  
  // Agregar socio
  document.getElementById('formulario-agregar-socio').addEventListener('submit', (e) => {
    e.preventDefault();
    const nombre_socio = document.getElementById('nombre_socio').value;
    const apellido_socio = document.getElementById('apellido_socio').value;
    const correo_electronico_socio = document.getElementById('correo_electronico_socio').value;
    const telefono_socio = document.getElementById('telefono_socio').value;
    fetch('/agregar-socio', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre_socio, apellido_socio, correo_electronico_socio, telefono_socio })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
  });