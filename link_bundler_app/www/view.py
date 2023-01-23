import frappe

def get_context(context):
    context.bundles = frappe.get_list("Bundle Doc", fields=["title", "description", "password"])
    return context

