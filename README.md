# django_xss_protector

djago xss protector is a Python library for filtering incomming requests with malformed data in view level

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django_xss_protector.

```bash
pip install django_xss_protector
```

## import it in your view

```python
from xss_protector.decorator import xss_protector 
```

## filter all

```python
@xss_protector()
def my_view(reqeust):
    ....

```
this will check everything, the url parameters, url querystring, request body and form data for possible xss data

## filter some keys

```python
@xss_protector("key1", "key2", "key3")
def my_view(reqeust):
    ....

```
this will check the url parameters, url querystring, request body and form data for possible xss data but only in the mentioned keys

## exclude some keys

```python
@xss_protector(lst_excluding_keys=["key1", "key2"])
def my_view(reqeust):
    ....

```
this will check the url parameters, url querystring, request body and form data for possible xss data but not in the mentioned keys

## custome response

```python
@xss_protector(response_on_error=JsonResponse({"ERROR": "custome error"})
def my_view(reqeust):
    ....

```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit)
