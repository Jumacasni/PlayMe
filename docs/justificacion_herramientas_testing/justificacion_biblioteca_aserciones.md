# Elección de biblioteca de aserciones y justificación

Las bibliotecas de aserciones que pueden usarse en este proyecto y que se van a discutir son:
- Grappa
- AssertPy
- Verify

---
## Grappa

**Ventajas :white_check_mark:**
- Se entiende muy fácil la intención del código debido a su fácil legibilidad
```python
3.14 | should.be.lower.than(4)

```
- Se tienen dos estilos de declaración: ```expect``` y ```should```
```python
'foo' | should.be.equal.to('foo')
[1, 2, 3] | expect.to.contain([2, 3])
```
- Dos maneras diferentes de escribir una misma aserción
```python
should('foo').be.equal.to('foo')
'foo' | should.be.equal.to('foo')
```

**Ejemplo de uso :desktop_computer:**

Se puede ver un ejemplo de uso de Grappa aplicado a este proyecto en el [commit #1e22c3f](https://github.com/Jumacasni/PlayMe/commit/1e22c3fef7d3211decea78925d610bfd47d3b034)

---
## AssertPy

**Ventajas :white_check_mark:**
- Sólo se importa una función para usarlo: ```assert_that()```
- Las funciones llaman a métodos que son fáciles de leer gracias a sus nombres
```python
assert_that('hello').is_equal_to('hello')
```
- Soporta valores de ```datetime```, ```files``` y objetos
```python
assert_that(x).has_year(1980)
```
- Soporta llamadas a funciones que comprueban directamente tests relacionados con listas
```python
assert_that(['a','b']).is_length(2)
assert_that(['a','b']).contains('b','a')
```

**Ejemplo de uso :desktop_computer:**

Se puede ver un ejemplo de uso de AssertPy aplicado a este proyecto en el [commit #8e083ce](https://github.com/Jumacasni/PlayMe/commit/8e083cea49866a19a004e4c208a6ab6e1c89b9ce)

---
## Verify

**Ventajas :white_check_mark:**
- Varias sintaxis disponibles para asegurar un lenguaje natural:
	- Uso de ```expect``` con ```to be```
	```python
	expect(something).to_be_int().to_be_less_or_equal(5).to_be_greater_or_equal(1)
	```
	- Uso de ```ensure``` con ```is```
	```python
	ensure(something).is_int().is_less_or_equal(5).is_greater_or_equal(1)
	```
	- Uso de ```expect``` o ```ensure```
	```python
	ensure(something).Int().LessOrEqual(5).GreaterOrEqual(1)
	expect(something_else).Float().Number()
	```
- Se pueden hacer aserciones simplemente con ```verify```:
```python
import verify

verify.Truthy(1)
verify.Equal(2, 2)
verify.Greater(3, 2)
```

**Ejemplo de uso :desktop_computer:**

Se puede ver un ejemplo de uso de AssertPy aplicado a este proyecto en el [commit #8443dc0](https://github.com/Jumacasni/PlayMe/commit/8443dc0dec61ce06c5fe4173389830a41337af97)

---
## Conclusión

Definitivamente se descarta ```Verify``` porque su documentación puede llegar a ser confusa y no está actualizada.

Finalmente se decide usar ```AssertPy``` porque ofrece un lenguaje mucho más natural y más legible a simple vista para cualquier persona. Además, incluye aserciones sobre fechas que son importantes en este proyecto.

---
## Referencias

- [Grappa](https://grappa.readthedocs.io/en/latest/)
- [AssertPy](https://github.com/assertpy/assertpy)
- [Verify](https://verify.readthedocs.io/en/latest/index.html)