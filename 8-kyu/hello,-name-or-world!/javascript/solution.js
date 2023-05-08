const hello = (name="World") => `Hello, ${name ? name[0].toUpperCase() + name.slice(1).toLowerCase() : "World"}!`
