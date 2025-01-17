#include <iostream>
#include <vector>
#include <mfplay.h>
#include <python.h>
#include "capture/capture.h"

using namespace std;

vector< string > _get_devices(bool friendly) {
    vector< string > result;
    DeviceList  g_devices;
    HRESULT hr = S_OK;

    WCHAR* szFriendlyName = NULL;
    g_devices.Clear();

    hr = g_devices.EnumerateDevices();

    if (FAILED(hr)) {
        return result;
    }

    for (UINT32 iDevice = 0; iDevice < g_devices.Count(); iDevice++)
    {
        if(friendly){
            hr = g_devices.GetDeviceFriendlyName(iDevice, &szFriendlyName);
		}else{
            hr = g_devices.GetDeviceName(iDevice, &szFriendlyName);
		}
        if (FAILED(hr)) { return result; }
        wstring ws(szFriendlyName);
        string szFriendlyNameStr(ws.begin(), ws.end());
        result.push_back(szFriendlyNameStr);
        CoTaskMemFree(szFriendlyName);
        szFriendlyName = NULL;
    }
    return result;
}

PyObject* get_MF_devices(PyObject* self, PyObject* args) {
    vector< string > devices = _get_devices(false);
    PyObject* result = PyList_New(devices.size());
    for (int i = 0; i < devices.size(); ++i) {
        PyObject* pytmp = Py_BuildValue("s", devices[i].c_str());
        PyList_SetItem(result, i, pytmp);
    }
    return result;
}

PyObject* get_MF_friendly_devices(PyObject* self, PyObject* args) {
    vector< string > devices = _get_devices(true);
    PyObject* result = PyList_New(devices.size());
    for (int i = 0; i < devices.size(); ++i) {
        PyObject* pytmp = Py_BuildValue("s", devices[i].c_str());
        PyList_SetItem(result, i, pytmp);
    }
    return result;
}

static PyMethodDef cv_camera_finder_methods[] = {
    // The first property is the name exposed to Python, fast_tanh, the second is the C++
    // function name that contains the implementation.
    { "get_MF_devices", (PyCFunction)get_MF_devices, METH_NOARGS, nullptr },
    { "get_MF_friendly_devices", (PyCFunction)get_MF_friendly_devices, METH_NOARGS, nullptr },

    // Terminate the array with an object containing nulls.
    { nullptr, nullptr, 0, nullptr }
};

static PyModuleDef cv_camera_finder_module = {
    PyModuleDef_HEAD_INIT,
    "cv_camera_finder",                        // Module name to use with Python import statements
    "MSMF tool",                    // Module description
    0,
    cv_camera_finder_methods                   // Structure that defines the methods of the module
};

PyMODINIT_FUNC PyInit_cv_camera_finder() {
    return PyModule_Create(&cv_camera_finder_module);
}
