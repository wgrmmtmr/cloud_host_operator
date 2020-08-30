from nslookup import Nslookup

def getmyip():
    domain = "myip.opendns.com"

    dns_query = Nslookup(dns_servers=["208.67.220.220"])

    ips_record = dns_query.dns_lookup(domain)

    #print(ips_record.response_full, ips_record.answer)

    if(len(ips_record.answer) == 0):
        print("Query My IP from opendns failed")

    return ips_record.answer[0]


if __name__ == "__main__":
    print(getmyip())

