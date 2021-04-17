def subdomainVisitCount(visits):
    visitCount = {}
    subDomains = []
    for visit in visits:
        count, domain = visit.split(" ")
        count = int(count)
        visitCount[domain] = count
        subDomains.append(domain)
        while "." in domain:
            domain = domain[domain.find(".")+1:]
            if domain not in visitCount.keys():
                visitCount[domain] = count
                subDomains.append(domain)
            else:
                visitCount[domain] += count
    res = []
    for domain in subDomains:
        res.append(str(visitCount[domain])+" "+domain)
    return res


subdomainVisitCount(["9001 discuss.leetcode.com"])
subdomainVisitCount(["900 google.mail.com", "50 yahoo.com",
                     "1 intel.mail.com", "5 wiki.org"])
