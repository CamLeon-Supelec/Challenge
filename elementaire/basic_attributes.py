#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse_elementary_attributes(records):
    # record = (process, RIP, API_call)
    n_RIP = len(records)
    API_calls = []
    processes = []
    
    for record in records:
        process = records[0]
        if not process in processes:
            processes.append(process)

        API_call = record[2]
        if not API_call in API_calls:
            API_calls.append(API_call)

    n_API_calls = len(API_calls)
    n_processes = len(processes)

    return n_RIP, n_API_calls, n_processes

