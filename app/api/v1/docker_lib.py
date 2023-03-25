import docker


if __name__ == "__main__":
    client = docker.client.from_env()
    print(client.containers.list())
    # first = client.containers.list()[0]
    first = client.containers.get("1781fe434860")
    print(first, first.__dir__())
    # print(first.status())
    # print(first.collection())
    # for item in first.stats():
    #     print(item)
    print(first.top())
    # first.
