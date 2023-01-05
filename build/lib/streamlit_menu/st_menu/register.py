from streamlit import session_state as _state
from streamlit.components.v1 import components as _components


def _patch_register_widget(register_widget):

    def wrapper_register_widget(*args, **kwargs):
        user_key = kwargs.get("user_key", None)
        callbacks = _state.get("_components_callbacks", None)
        # Check if a callback was registered for that user_key.
        if user_key and callbacks and user_key in callbacks:
            callback = callbacks[user_key]
            # Add callback-specific args for the real register_widget function.
            kwargs["on_change_handler"] = callback[0]
            kwargs["args"] = callback[1]
            kwargs["kwargs"] = callback[2]
        # Call the original function with updated kwargs.
        result = register_widget(*args, **kwargs)
        return result

    return wrapper_register_widget


# Patch function only once.


def init():
    if not hasattr(_components.register_widget, "__callbacks_patched__"):
        setattr(_components.register_widget, "__callbacks_patched__", True)
        _components.register_widget = _patch_register_widget(
            _components.register_widget)


def register_callback(element_key, callback, *callback_args,
                      **callback_kwargs):
    # Initialize callbacks store.
    if "_components_callbacks" not in _state:
        _state._components_callbacks = {}
    # Register a callback for a given element_key.
    _state._components_callbacks[element_key] = (callback, callback_args,
                                                 callback_kwargs)


def get_component_rerender_count(element_key):
    # This funtion will return the custom component render count
    if "_component_render_count" not in _state:
        _state["_component_render_count"] = {}
    if element_key not in _state["_component_render_count"]:
        _state["_component_render_count"][element_key] = 0
    return _state["_component_render_count"][element_key]


def set_component_rerender_count(element_key):
    # This funtion will record the rerendering count
    _state["_component_render_count"][
        element_key] = get_component_rerender_count(element_key) + 1
    return _state["_component_render_count"][element_key]
