import ansible_runner


def hello():
    print("World")


def run(path):
    r = ansible_runner.run(
        private_data_dir='./',
        playbook=path,
        extravars={'foo': 'bar'})
    # print("{}: {}".format(r.status, r.rc))
    # successful: 0
    # for each_host_event in r.events:
    #     print(each_host_event['event'])
    #     print("Final status:")
    #     print(r.stats)


def run2():
    r = ansible_runner.run(
        private_data_dir='./',
        playbook='site.yml',
        inventory='hosts',
        extravars={'foo': 'bar'})
