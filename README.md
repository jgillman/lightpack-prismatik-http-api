# Lightpack + Prismatik HTTP API

A small http server for controlling a [Lightpack][] via Prismatik's API.


I'm using it in conjunction with [homebridge-http](https://github.com/rudders/homebridge-http)
so that I can control my [Lightpack][] via HomeKit and Siri.

## Install

Clone the repo

```sh
git clone git@github.com:jgillman/lightpack-prismatik-http-api.git lightpack
```

Set up the virtualenv

```sh
virtualenv lightpack
cd lightpack
source bin/activate
```

Install the requirements

```sh
pip install -r requirements.txt
```

## Configure

Update the variables in `mypack/__init__.py` if you use a different host/port
or use an api\_key.

## Usage

Get the current status (as json):

```sh
$ curl "http://localhost:8080/lightpack"
```

Turn it on:

```sh
curl "http://localhost:8080/lightpack/on"
```

Turn it off:

```sh
curl "http://localhost:8080/lightpack/off"
```

Change to profile `PROFILE_NAME`:

```sh
curl "http://localhost:8080/lightpack/profile/PROFILE_NAME"
```

## Responses

Successful requests get a 200 with a body of JSON:

```javascript
{
  'power': 'on',
  'profile': 'Lightpack'
}
```

Bad requests get a 404 with no body.

---

# Disclaimer

1. This is the first Python I've ever written and I make no claims to it's
   quality or style.
2. I wrote this for myself so its portability between systems is questionable
   at best 😄


[Lightpack]: http://lightpack.tv/
