# Products

Create an application that can display products.

- You shall not change the given data structures.
- The template can only receive a list.
- You must create the template based on the provided HTML
  - Use variables, for loops and filters
  - The price must be rounded with precision 2

## Python boilerplate

```python
products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)
]
```

## The rendered template

```html
<table>
  <tr>
    <th>#</th>
    <th>Product</th>
    <th>Price</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Milk</td>
    <td>3.59 ¥</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Bread</td>
    <td>2.96 ¥</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Rice</td>
    <td>0.64 ¥</td>
  </tr>
</table>
```