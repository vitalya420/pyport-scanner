import port_scanner


def on_port_opened(task: str, ip, port, status):
    print("task {task}", ip, port, status)


def main():
    task_name = "my_port_scan_task"
    port_scanner.syn_scan(
        "192.168.0.0/28",
        [80, 255],
        5,
        callback=lambda r: on_port_opened(task_name, *r),
    )


if __name__ == "__main__":
    main()
