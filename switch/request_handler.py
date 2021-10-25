# -*- coding: utf-8 -*-

def get_request(server, line):
    URL = server.domain + server.path
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'Bearer ' + server.token}
    data = {'qty': line.qty, 'inferiorQty': line.errorQty, 'produceLineId': line.id}
    return {
      URL: URL,
      headers: headers,
      data: data
    }
