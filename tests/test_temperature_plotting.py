#!/usr/bin/env python
# coding: utf-8

import pytest, os

import temperature_plotting as tpl


def test_compute_mean():
    calc = tpl.compute_mean([0,10,20])
    assert calc == 10
    assert type(calc) == float
    
    calc = tpl.compute_mean([-10, 10])
    assert calc == 0
    
    calc = tpl.compute_mean([0,10,0])
    assert round(calc,4) == 3.3333, "check that the average is roughly correct"
    
    with pytest.raises(TypeError):
        calc = tpl.compute_mean(["a","b","c"])
        #calc = tpl.compute_mean([-10, 10])
        
    calc = tpl.compute_mean([])
    assert calc == None
    
@pytest.mark.skip(reason="test is made to fail")
def test_create_name():
    assert tpl.create_name(77) == "plot_7778.png"
    assert tpl.create_name("") == "plot_.png"
    assert tpl.create_name("fifteen") == "plot_fifteen.png"

    with pytest.raises(TypeError):
        tpl.create_name()
        
# integration test
def test_main():
    tpl.main()
    assert os.path.exists("plot_25.png")
    
