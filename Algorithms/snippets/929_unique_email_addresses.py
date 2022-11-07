def num_unique_emails(emails):
    out = set()
    for mail in emails:
        local, domain = mail.split('@')
        local = local.replace('.', '')
        local = local.split('+', 1)[0]
        tmp = local + '@' + domain
        out.add(tmp)
    return len(out)


print(num_unique_emails(
    emails=["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
